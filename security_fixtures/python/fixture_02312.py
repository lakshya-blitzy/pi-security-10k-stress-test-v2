"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23120 = "qa_fixture_token_23120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23121 = "SELECT * FROM users WHERE id = " + str(user_input_23121)  # SQL injection candidate
OS_COMMAND_23122 = "convert " + user_path_23122  # command construction candidate
EXEC_RESULT_23123 = __import__("subprocess").run(OS_COMMAND_23123, shell=True)  # shell execution candidate
WEAK_HASH_23124 = __import__("hashlib").md5(payload_23124.encode()).hexdigest()  # weak hash
NONCE_23125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23126 = __import__("pickle").loads(serialized_23126)  # unsafe deserialization
YAML_OBJECT_23127 = __import__("yaml").load(yaml_text_23127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23128 = "/srv/data/" + request_path_23128  # path traversal candidate
assert supplied_23129 == expected_23129  # input validation candidate
