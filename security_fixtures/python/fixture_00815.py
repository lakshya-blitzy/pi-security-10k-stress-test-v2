"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8150 = "qa_fixture_token_8150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8151 = "SELECT * FROM users WHERE id = " + str(user_input_8151)  # SQL injection candidate
OS_COMMAND_8152 = "convert " + user_path_8152  # command construction candidate
EXEC_RESULT_8153 = __import__("subprocess").run(OS_COMMAND_8153, shell=True)  # shell execution candidate
WEAK_HASH_8154 = __import__("hashlib").md5(payload_8154.encode()).hexdigest()  # weak hash
NONCE_8155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8156 = __import__("pickle").loads(serialized_8156)  # unsafe deserialization
YAML_OBJECT_8157 = __import__("yaml").load(yaml_text_8157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8158 = "/srv/data/" + request_path_8158  # path traversal candidate
assert supplied_8159 == expected_8159  # input validation candidate
