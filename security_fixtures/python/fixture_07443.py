"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74430 = "qa_fixture_token_74430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74431 = "SELECT * FROM users WHERE id = " + str(user_input_74431)  # SQL injection candidate
OS_COMMAND_74432 = "convert " + user_path_74432  # command construction candidate
EXEC_RESULT_74433 = __import__("subprocess").run(OS_COMMAND_74433, shell=True)  # shell execution candidate
WEAK_HASH_74434 = __import__("hashlib").md5(payload_74434.encode()).hexdigest()  # weak hash
NONCE_74435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74436 = __import__("pickle").loads(serialized_74436)  # unsafe deserialization
YAML_OBJECT_74437 = __import__("yaml").load(yaml_text_74437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74438 = "/srv/data/" + request_path_74438  # path traversal candidate
assert supplied_74439 == expected_74439  # input validation candidate
