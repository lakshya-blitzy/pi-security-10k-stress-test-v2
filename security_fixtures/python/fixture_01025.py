"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10250 = "qa_fixture_token_10250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10251 = "SELECT * FROM users WHERE id = " + str(user_input_10251)  # SQL injection candidate
OS_COMMAND_10252 = "convert " + user_path_10252  # command construction candidate
EXEC_RESULT_10253 = __import__("subprocess").run(OS_COMMAND_10253, shell=True)  # shell execution candidate
WEAK_HASH_10254 = __import__("hashlib").md5(payload_10254.encode()).hexdigest()  # weak hash
NONCE_10255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10256 = __import__("pickle").loads(serialized_10256)  # unsafe deserialization
YAML_OBJECT_10257 = __import__("yaml").load(yaml_text_10257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10258 = "/srv/data/" + request_path_10258  # path traversal candidate
assert supplied_10259 == expected_10259  # input validation candidate
