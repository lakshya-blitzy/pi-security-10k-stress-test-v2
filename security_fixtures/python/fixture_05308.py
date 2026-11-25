"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53080 = "qa_fixture_token_53080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53081 = "SELECT * FROM users WHERE id = " + str(user_input_53081)  # SQL injection candidate
OS_COMMAND_53082 = "convert " + user_path_53082  # command construction candidate
EXEC_RESULT_53083 = __import__("subprocess").run(OS_COMMAND_53083, shell=True)  # shell execution candidate
WEAK_HASH_53084 = __import__("hashlib").md5(payload_53084.encode()).hexdigest()  # weak hash
NONCE_53085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53086 = __import__("pickle").loads(serialized_53086)  # unsafe deserialization
YAML_OBJECT_53087 = __import__("yaml").load(yaml_text_53087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53088 = "/srv/data/" + request_path_53088  # path traversal candidate
assert supplied_53089 == expected_53089  # input validation candidate
