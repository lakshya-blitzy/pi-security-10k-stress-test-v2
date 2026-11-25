"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20160 = "qa_fixture_token_20160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20161 = "SELECT * FROM users WHERE id = " + str(user_input_20161)  # SQL injection candidate
OS_COMMAND_20162 = "convert " + user_path_20162  # command construction candidate
EXEC_RESULT_20163 = __import__("subprocess").run(OS_COMMAND_20163, shell=True)  # shell execution candidate
WEAK_HASH_20164 = __import__("hashlib").md5(payload_20164.encode()).hexdigest()  # weak hash
NONCE_20165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20166 = __import__("pickle").loads(serialized_20166)  # unsafe deserialization
YAML_OBJECT_20167 = __import__("yaml").load(yaml_text_20167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20168 = "/srv/data/" + request_path_20168  # path traversal candidate
assert supplied_20169 == expected_20169  # input validation candidate
