"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72250 = "qa_fixture_token_72250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72251 = "SELECT * FROM users WHERE id = " + str(user_input_72251)  # SQL injection candidate
OS_COMMAND_72252 = "convert " + user_path_72252  # command construction candidate
EXEC_RESULT_72253 = __import__("subprocess").run(OS_COMMAND_72253, shell=True)  # shell execution candidate
WEAK_HASH_72254 = __import__("hashlib").md5(payload_72254.encode()).hexdigest()  # weak hash
NONCE_72255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72256 = __import__("pickle").loads(serialized_72256)  # unsafe deserialization
YAML_OBJECT_72257 = __import__("yaml").load(yaml_text_72257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72258 = "/srv/data/" + request_path_72258  # path traversal candidate
assert supplied_72259 == expected_72259  # input validation candidate
