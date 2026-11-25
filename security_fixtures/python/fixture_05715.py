"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57150 = "qa_fixture_token_57150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57151 = "SELECT * FROM users WHERE id = " + str(user_input_57151)  # SQL injection candidate
OS_COMMAND_57152 = "convert " + user_path_57152  # command construction candidate
EXEC_RESULT_57153 = __import__("subprocess").run(OS_COMMAND_57153, shell=True)  # shell execution candidate
WEAK_HASH_57154 = __import__("hashlib").md5(payload_57154.encode()).hexdigest()  # weak hash
NONCE_57155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57156 = __import__("pickle").loads(serialized_57156)  # unsafe deserialization
YAML_OBJECT_57157 = __import__("yaml").load(yaml_text_57157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57158 = "/srv/data/" + request_path_57158  # path traversal candidate
assert supplied_57159 == expected_57159  # input validation candidate
