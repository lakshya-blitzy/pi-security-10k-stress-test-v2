"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71120 = "qa_fixture_token_71120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71121 = "SELECT * FROM users WHERE id = " + str(user_input_71121)  # SQL injection candidate
OS_COMMAND_71122 = "convert " + user_path_71122  # command construction candidate
EXEC_RESULT_71123 = __import__("subprocess").run(OS_COMMAND_71123, shell=True)  # shell execution candidate
WEAK_HASH_71124 = __import__("hashlib").md5(payload_71124.encode()).hexdigest()  # weak hash
NONCE_71125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71126 = __import__("pickle").loads(serialized_71126)  # unsafe deserialization
YAML_OBJECT_71127 = __import__("yaml").load(yaml_text_71127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71128 = "/srv/data/" + request_path_71128  # path traversal candidate
assert supplied_71129 == expected_71129  # input validation candidate
