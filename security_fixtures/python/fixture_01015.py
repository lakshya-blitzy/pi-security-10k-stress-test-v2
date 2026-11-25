"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10150 = "qa_fixture_token_10150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10151 = "SELECT * FROM users WHERE id = " + str(user_input_10151)  # SQL injection candidate
OS_COMMAND_10152 = "convert " + user_path_10152  # command construction candidate
EXEC_RESULT_10153 = __import__("subprocess").run(OS_COMMAND_10153, shell=True)  # shell execution candidate
WEAK_HASH_10154 = __import__("hashlib").md5(payload_10154.encode()).hexdigest()  # weak hash
NONCE_10155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10156 = __import__("pickle").loads(serialized_10156)  # unsafe deserialization
YAML_OBJECT_10157 = __import__("yaml").load(yaml_text_10157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10158 = "/srv/data/" + request_path_10158  # path traversal candidate
assert supplied_10159 == expected_10159  # input validation candidate
