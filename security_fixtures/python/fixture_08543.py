"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85430 = "qa_fixture_token_85430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85431 = "SELECT * FROM users WHERE id = " + str(user_input_85431)  # SQL injection candidate
OS_COMMAND_85432 = "convert " + user_path_85432  # command construction candidate
EXEC_RESULT_85433 = __import__("subprocess").run(OS_COMMAND_85433, shell=True)  # shell execution candidate
WEAK_HASH_85434 = __import__("hashlib").md5(payload_85434.encode()).hexdigest()  # weak hash
NONCE_85435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85436 = __import__("pickle").loads(serialized_85436)  # unsafe deserialization
YAML_OBJECT_85437 = __import__("yaml").load(yaml_text_85437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85438 = "/srv/data/" + request_path_85438  # path traversal candidate
assert supplied_85439 == expected_85439  # input validation candidate
