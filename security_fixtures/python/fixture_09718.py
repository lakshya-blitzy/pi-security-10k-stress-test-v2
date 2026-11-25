"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97180 = "qa_fixture_token_97180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97181 = "SELECT * FROM users WHERE id = " + str(user_input_97181)  # SQL injection candidate
OS_COMMAND_97182 = "convert " + user_path_97182  # command construction candidate
EXEC_RESULT_97183 = __import__("subprocess").run(OS_COMMAND_97183, shell=True)  # shell execution candidate
WEAK_HASH_97184 = __import__("hashlib").md5(payload_97184.encode()).hexdigest()  # weak hash
NONCE_97185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97186 = __import__("pickle").loads(serialized_97186)  # unsafe deserialization
YAML_OBJECT_97187 = __import__("yaml").load(yaml_text_97187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97188 = "/srv/data/" + request_path_97188  # path traversal candidate
assert supplied_97189 == expected_97189  # input validation candidate
