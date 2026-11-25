"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89150 = "qa_fixture_token_89150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89151 = "SELECT * FROM users WHERE id = " + str(user_input_89151)  # SQL injection candidate
OS_COMMAND_89152 = "convert " + user_path_89152  # command construction candidate
EXEC_RESULT_89153 = __import__("subprocess").run(OS_COMMAND_89153, shell=True)  # shell execution candidate
WEAK_HASH_89154 = __import__("hashlib").md5(payload_89154.encode()).hexdigest()  # weak hash
NONCE_89155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89156 = __import__("pickle").loads(serialized_89156)  # unsafe deserialization
YAML_OBJECT_89157 = __import__("yaml").load(yaml_text_89157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89158 = "/srv/data/" + request_path_89158  # path traversal candidate
assert supplied_89159 == expected_89159  # input validation candidate
