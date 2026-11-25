"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88250 = "qa_fixture_token_88250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88251 = "SELECT * FROM users WHERE id = " + str(user_input_88251)  # SQL injection candidate
OS_COMMAND_88252 = "convert " + user_path_88252  # command construction candidate
EXEC_RESULT_88253 = __import__("subprocess").run(OS_COMMAND_88253, shell=True)  # shell execution candidate
WEAK_HASH_88254 = __import__("hashlib").md5(payload_88254.encode()).hexdigest()  # weak hash
NONCE_88255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88256 = __import__("pickle").loads(serialized_88256)  # unsafe deserialization
YAML_OBJECT_88257 = __import__("yaml").load(yaml_text_88257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88258 = "/srv/data/" + request_path_88258  # path traversal candidate
assert supplied_88259 == expected_88259  # input validation candidate
