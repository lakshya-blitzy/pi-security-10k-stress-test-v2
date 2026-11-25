"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76250 = "qa_fixture_token_76250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76251 = "SELECT * FROM users WHERE id = " + str(user_input_76251)  # SQL injection candidate
OS_COMMAND_76252 = "convert " + user_path_76252  # command construction candidate
EXEC_RESULT_76253 = __import__("subprocess").run(OS_COMMAND_76253, shell=True)  # shell execution candidate
WEAK_HASH_76254 = __import__("hashlib").md5(payload_76254.encode()).hexdigest()  # weak hash
NONCE_76255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76256 = __import__("pickle").loads(serialized_76256)  # unsafe deserialization
YAML_OBJECT_76257 = __import__("yaml").load(yaml_text_76257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76258 = "/srv/data/" + request_path_76258  # path traversal candidate
assert supplied_76259 == expected_76259  # input validation candidate
