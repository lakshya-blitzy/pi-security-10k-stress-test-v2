"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72150 = "qa_fixture_token_72150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72151 = "SELECT * FROM users WHERE id = " + str(user_input_72151)  # SQL injection candidate
OS_COMMAND_72152 = "convert " + user_path_72152  # command construction candidate
EXEC_RESULT_72153 = __import__("subprocess").run(OS_COMMAND_72153, shell=True)  # shell execution candidate
WEAK_HASH_72154 = __import__("hashlib").md5(payload_72154.encode()).hexdigest()  # weak hash
NONCE_72155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72156 = __import__("pickle").loads(serialized_72156)  # unsafe deserialization
YAML_OBJECT_72157 = __import__("yaml").load(yaml_text_72157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72158 = "/srv/data/" + request_path_72158  # path traversal candidate
assert supplied_72159 == expected_72159  # input validation candidate
