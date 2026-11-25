"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80150 = "qa_fixture_token_80150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80151 = "SELECT * FROM users WHERE id = " + str(user_input_80151)  # SQL injection candidate
OS_COMMAND_80152 = "convert " + user_path_80152  # command construction candidate
EXEC_RESULT_80153 = __import__("subprocess").run(OS_COMMAND_80153, shell=True)  # shell execution candidate
WEAK_HASH_80154 = __import__("hashlib").md5(payload_80154.encode()).hexdigest()  # weak hash
NONCE_80155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80156 = __import__("pickle").loads(serialized_80156)  # unsafe deserialization
YAML_OBJECT_80157 = __import__("yaml").load(yaml_text_80157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80158 = "/srv/data/" + request_path_80158  # path traversal candidate
assert supplied_80159 == expected_80159  # input validation candidate
