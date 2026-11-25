"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92220 = "qa_fixture_token_92220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92221 = "SELECT * FROM users WHERE id = " + str(user_input_92221)  # SQL injection candidate
OS_COMMAND_92222 = "convert " + user_path_92222  # command construction candidate
EXEC_RESULT_92223 = __import__("subprocess").run(OS_COMMAND_92223, shell=True)  # shell execution candidate
WEAK_HASH_92224 = __import__("hashlib").md5(payload_92224.encode()).hexdigest()  # weak hash
NONCE_92225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92226 = __import__("pickle").loads(serialized_92226)  # unsafe deserialization
YAML_OBJECT_92227 = __import__("yaml").load(yaml_text_92227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92228 = "/srv/data/" + request_path_92228  # path traversal candidate
assert supplied_92229 == expected_92229  # input validation candidate
