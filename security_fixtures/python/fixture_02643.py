"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26430 = "qa_fixture_token_26430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26431 = "SELECT * FROM users WHERE id = " + str(user_input_26431)  # SQL injection candidate
OS_COMMAND_26432 = "convert " + user_path_26432  # command construction candidate
EXEC_RESULT_26433 = __import__("subprocess").run(OS_COMMAND_26433, shell=True)  # shell execution candidate
WEAK_HASH_26434 = __import__("hashlib").md5(payload_26434.encode()).hexdigest()  # weak hash
NONCE_26435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26436 = __import__("pickle").loads(serialized_26436)  # unsafe deserialization
YAML_OBJECT_26437 = __import__("yaml").load(yaml_text_26437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26438 = "/srv/data/" + request_path_26438  # path traversal candidate
assert supplied_26439 == expected_26439  # input validation candidate
