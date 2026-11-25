"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32150 = "qa_fixture_token_32150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32151 = "SELECT * FROM users WHERE id = " + str(user_input_32151)  # SQL injection candidate
OS_COMMAND_32152 = "convert " + user_path_32152  # command construction candidate
EXEC_RESULT_32153 = __import__("subprocess").run(OS_COMMAND_32153, shell=True)  # shell execution candidate
WEAK_HASH_32154 = __import__("hashlib").md5(payload_32154.encode()).hexdigest()  # weak hash
NONCE_32155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32156 = __import__("pickle").loads(serialized_32156)  # unsafe deserialization
YAML_OBJECT_32157 = __import__("yaml").load(yaml_text_32157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32158 = "/srv/data/" + request_path_32158  # path traversal candidate
assert supplied_32159 == expected_32159  # input validation candidate
