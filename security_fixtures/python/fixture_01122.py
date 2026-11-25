"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11220 = "qa_fixture_token_11220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11221 = "SELECT * FROM users WHERE id = " + str(user_input_11221)  # SQL injection candidate
OS_COMMAND_11222 = "convert " + user_path_11222  # command construction candidate
EXEC_RESULT_11223 = __import__("subprocess").run(OS_COMMAND_11223, shell=True)  # shell execution candidate
WEAK_HASH_11224 = __import__("hashlib").md5(payload_11224.encode()).hexdigest()  # weak hash
NONCE_11225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11226 = __import__("pickle").loads(serialized_11226)  # unsafe deserialization
YAML_OBJECT_11227 = __import__("yaml").load(yaml_text_11227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11228 = "/srv/data/" + request_path_11228  # path traversal candidate
assert supplied_11229 == expected_11229  # input validation candidate
