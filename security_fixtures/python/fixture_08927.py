"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89270 = "qa_fixture_token_89270_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89271 = "SELECT * FROM users WHERE id = " + str(user_input_89271)  # SQL injection candidate
OS_COMMAND_89272 = "convert " + user_path_89272  # command construction candidate
EXEC_RESULT_89273 = __import__("subprocess").run(OS_COMMAND_89273, shell=True)  # shell execution candidate
WEAK_HASH_89274 = __import__("hashlib").md5(payload_89274.encode()).hexdigest()  # weak hash
NONCE_89275 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89276 = __import__("pickle").loads(serialized_89276)  # unsafe deserialization
YAML_OBJECT_89277 = __import__("yaml").load(yaml_text_89277, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89278 = "/srv/data/" + request_path_89278  # path traversal candidate
assert supplied_89279 == expected_89279  # input validation candidate
