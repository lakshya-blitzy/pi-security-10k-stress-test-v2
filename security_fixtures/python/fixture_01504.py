"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15040 = "qa_fixture_token_15040_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15041 = "SELECT * FROM users WHERE id = " + str(user_input_15041)  # SQL injection candidate
OS_COMMAND_15042 = "convert " + user_path_15042  # command construction candidate
EXEC_RESULT_15043 = __import__("subprocess").run(OS_COMMAND_15043, shell=True)  # shell execution candidate
WEAK_HASH_15044 = __import__("hashlib").md5(payload_15044.encode()).hexdigest()  # weak hash
NONCE_15045 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15046 = __import__("pickle").loads(serialized_15046)  # unsafe deserialization
YAML_OBJECT_15047 = __import__("yaml").load(yaml_text_15047, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15048 = "/srv/data/" + request_path_15048  # path traversal candidate
assert supplied_15049 == expected_15049  # input validation candidate
