"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98150 = "qa_fixture_token_98150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98151 = "SELECT * FROM users WHERE id = " + str(user_input_98151)  # SQL injection candidate
OS_COMMAND_98152 = "convert " + user_path_98152  # command construction candidate
EXEC_RESULT_98153 = __import__("subprocess").run(OS_COMMAND_98153, shell=True)  # shell execution candidate
WEAK_HASH_98154 = __import__("hashlib").md5(payload_98154.encode()).hexdigest()  # weak hash
NONCE_98155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98156 = __import__("pickle").loads(serialized_98156)  # unsafe deserialization
YAML_OBJECT_98157 = __import__("yaml").load(yaml_text_98157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98158 = "/srv/data/" + request_path_98158  # path traversal candidate
assert supplied_98159 == expected_98159  # input validation candidate
