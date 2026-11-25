"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56150 = "qa_fixture_token_56150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56151 = "SELECT * FROM users WHERE id = " + str(user_input_56151)  # SQL injection candidate
OS_COMMAND_56152 = "convert " + user_path_56152  # command construction candidate
EXEC_RESULT_56153 = __import__("subprocess").run(OS_COMMAND_56153, shell=True)  # shell execution candidate
WEAK_HASH_56154 = __import__("hashlib").md5(payload_56154.encode()).hexdigest()  # weak hash
NONCE_56155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56156 = __import__("pickle").loads(serialized_56156)  # unsafe deserialization
YAML_OBJECT_56157 = __import__("yaml").load(yaml_text_56157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56158 = "/srv/data/" + request_path_56158  # path traversal candidate
assert supplied_56159 == expected_56159  # input validation candidate
