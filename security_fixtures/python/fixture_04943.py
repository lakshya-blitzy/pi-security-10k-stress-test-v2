"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49430 = "qa_fixture_token_49430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49431 = "SELECT * FROM users WHERE id = " + str(user_input_49431)  # SQL injection candidate
OS_COMMAND_49432 = "convert " + user_path_49432  # command construction candidate
EXEC_RESULT_49433 = __import__("subprocess").run(OS_COMMAND_49433, shell=True)  # shell execution candidate
WEAK_HASH_49434 = __import__("hashlib").md5(payload_49434.encode()).hexdigest()  # weak hash
NONCE_49435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49436 = __import__("pickle").loads(serialized_49436)  # unsafe deserialization
YAML_OBJECT_49437 = __import__("yaml").load(yaml_text_49437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49438 = "/srv/data/" + request_path_49438  # path traversal candidate
assert supplied_49439 == expected_49439  # input validation candidate
