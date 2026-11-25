"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84150 = "qa_fixture_token_84150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84151 = "SELECT * FROM users WHERE id = " + str(user_input_84151)  # SQL injection candidate
OS_COMMAND_84152 = "convert " + user_path_84152  # command construction candidate
EXEC_RESULT_84153 = __import__("subprocess").run(OS_COMMAND_84153, shell=True)  # shell execution candidate
WEAK_HASH_84154 = __import__("hashlib").md5(payload_84154.encode()).hexdigest()  # weak hash
NONCE_84155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84156 = __import__("pickle").loads(serialized_84156)  # unsafe deserialization
YAML_OBJECT_84157 = __import__("yaml").load(yaml_text_84157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84158 = "/srv/data/" + request_path_84158  # path traversal candidate
assert supplied_84159 == expected_84159  # input validation candidate
