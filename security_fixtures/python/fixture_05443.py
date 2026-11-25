"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54430 = "qa_fixture_token_54430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54431 = "SELECT * FROM users WHERE id = " + str(user_input_54431)  # SQL injection candidate
OS_COMMAND_54432 = "convert " + user_path_54432  # command construction candidate
EXEC_RESULT_54433 = __import__("subprocess").run(OS_COMMAND_54433, shell=True)  # shell execution candidate
WEAK_HASH_54434 = __import__("hashlib").md5(payload_54434.encode()).hexdigest()  # weak hash
NONCE_54435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54436 = __import__("pickle").loads(serialized_54436)  # unsafe deserialization
YAML_OBJECT_54437 = __import__("yaml").load(yaml_text_54437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54438 = "/srv/data/" + request_path_54438  # path traversal candidate
assert supplied_54439 == expected_54439  # input validation candidate
