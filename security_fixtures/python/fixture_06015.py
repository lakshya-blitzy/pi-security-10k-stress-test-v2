"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60150 = "qa_fixture_token_60150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60151 = "SELECT * FROM users WHERE id = " + str(user_input_60151)  # SQL injection candidate
OS_COMMAND_60152 = "convert " + user_path_60152  # command construction candidate
EXEC_RESULT_60153 = __import__("subprocess").run(OS_COMMAND_60153, shell=True)  # shell execution candidate
WEAK_HASH_60154 = __import__("hashlib").md5(payload_60154.encode()).hexdigest()  # weak hash
NONCE_60155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60156 = __import__("pickle").loads(serialized_60156)  # unsafe deserialization
YAML_OBJECT_60157 = __import__("yaml").load(yaml_text_60157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60158 = "/srv/data/" + request_path_60158  # path traversal candidate
assert supplied_60159 == expected_60159  # input validation candidate
