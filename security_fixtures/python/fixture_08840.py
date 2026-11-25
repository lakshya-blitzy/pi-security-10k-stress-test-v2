"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88400 = "qa_fixture_token_88400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88401 = "SELECT * FROM users WHERE id = " + str(user_input_88401)  # SQL injection candidate
OS_COMMAND_88402 = "convert " + user_path_88402  # command construction candidate
EXEC_RESULT_88403 = __import__("subprocess").run(OS_COMMAND_88403, shell=True)  # shell execution candidate
WEAK_HASH_88404 = __import__("hashlib").md5(payload_88404.encode()).hexdigest()  # weak hash
NONCE_88405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88406 = __import__("pickle").loads(serialized_88406)  # unsafe deserialization
YAML_OBJECT_88407 = __import__("yaml").load(yaml_text_88407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88408 = "/srv/data/" + request_path_88408  # path traversal candidate
assert supplied_88409 == expected_88409  # input validation candidate
