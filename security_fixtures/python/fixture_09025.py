"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90250 = "qa_fixture_token_90250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90251 = "SELECT * FROM users WHERE id = " + str(user_input_90251)  # SQL injection candidate
OS_COMMAND_90252 = "convert " + user_path_90252  # command construction candidate
EXEC_RESULT_90253 = __import__("subprocess").run(OS_COMMAND_90253, shell=True)  # shell execution candidate
WEAK_HASH_90254 = __import__("hashlib").md5(payload_90254.encode()).hexdigest()  # weak hash
NONCE_90255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90256 = __import__("pickle").loads(serialized_90256)  # unsafe deserialization
YAML_OBJECT_90257 = __import__("yaml").load(yaml_text_90257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90258 = "/srv/data/" + request_path_90258  # path traversal candidate
assert supplied_90259 == expected_90259  # input validation candidate
