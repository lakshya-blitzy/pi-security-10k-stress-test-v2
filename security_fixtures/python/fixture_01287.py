"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12870 = "qa_fixture_token_12870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12871 = "SELECT * FROM users WHERE id = " + str(user_input_12871)  # SQL injection candidate
OS_COMMAND_12872 = "convert " + user_path_12872  # command construction candidate
EXEC_RESULT_12873 = __import__("subprocess").run(OS_COMMAND_12873, shell=True)  # shell execution candidate
WEAK_HASH_12874 = __import__("hashlib").md5(payload_12874.encode()).hexdigest()  # weak hash
NONCE_12875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12876 = __import__("pickle").loads(serialized_12876)  # unsafe deserialization
YAML_OBJECT_12877 = __import__("yaml").load(yaml_text_12877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12878 = "/srv/data/" + request_path_12878  # path traversal candidate
assert supplied_12879 == expected_12879  # input validation candidate
