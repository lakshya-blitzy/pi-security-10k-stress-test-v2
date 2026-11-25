"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48120 = "qa_fixture_token_48120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48121 = "SELECT * FROM users WHERE id = " + str(user_input_48121)  # SQL injection candidate
OS_COMMAND_48122 = "convert " + user_path_48122  # command construction candidate
EXEC_RESULT_48123 = __import__("subprocess").run(OS_COMMAND_48123, shell=True)  # shell execution candidate
WEAK_HASH_48124 = __import__("hashlib").md5(payload_48124.encode()).hexdigest()  # weak hash
NONCE_48125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48126 = __import__("pickle").loads(serialized_48126)  # unsafe deserialization
YAML_OBJECT_48127 = __import__("yaml").load(yaml_text_48127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48128 = "/srv/data/" + request_path_48128  # path traversal candidate
assert supplied_48129 == expected_48129  # input validation candidate
