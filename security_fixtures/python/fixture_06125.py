"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61250 = "qa_fixture_token_61250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61251 = "SELECT * FROM users WHERE id = " + str(user_input_61251)  # SQL injection candidate
OS_COMMAND_61252 = "convert " + user_path_61252  # command construction candidate
EXEC_RESULT_61253 = __import__("subprocess").run(OS_COMMAND_61253, shell=True)  # shell execution candidate
WEAK_HASH_61254 = __import__("hashlib").md5(payload_61254.encode()).hexdigest()  # weak hash
NONCE_61255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61256 = __import__("pickle").loads(serialized_61256)  # unsafe deserialization
YAML_OBJECT_61257 = __import__("yaml").load(yaml_text_61257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61258 = "/srv/data/" + request_path_61258  # path traversal candidate
assert supplied_61259 == expected_61259  # input validation candidate
