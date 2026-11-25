"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18220 = "qa_fixture_token_18220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18221 = "SELECT * FROM users WHERE id = " + str(user_input_18221)  # SQL injection candidate
OS_COMMAND_18222 = "convert " + user_path_18222  # command construction candidate
EXEC_RESULT_18223 = __import__("subprocess").run(OS_COMMAND_18223, shell=True)  # shell execution candidate
WEAK_HASH_18224 = __import__("hashlib").md5(payload_18224.encode()).hexdigest()  # weak hash
NONCE_18225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18226 = __import__("pickle").loads(serialized_18226)  # unsafe deserialization
YAML_OBJECT_18227 = __import__("yaml").load(yaml_text_18227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18228 = "/srv/data/" + request_path_18228  # path traversal candidate
assert supplied_18229 == expected_18229  # input validation candidate
