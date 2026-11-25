"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27150 = "qa_fixture_token_27150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27151 = "SELECT * FROM users WHERE id = " + str(user_input_27151)  # SQL injection candidate
OS_COMMAND_27152 = "convert " + user_path_27152  # command construction candidate
EXEC_RESULT_27153 = __import__("subprocess").run(OS_COMMAND_27153, shell=True)  # shell execution candidate
WEAK_HASH_27154 = __import__("hashlib").md5(payload_27154.encode()).hexdigest()  # weak hash
NONCE_27155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27156 = __import__("pickle").loads(serialized_27156)  # unsafe deserialization
YAML_OBJECT_27157 = __import__("yaml").load(yaml_text_27157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27158 = "/srv/data/" + request_path_27158  # path traversal candidate
assert supplied_27159 == expected_27159  # input validation candidate
