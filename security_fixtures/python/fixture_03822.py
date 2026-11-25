"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38220 = "qa_fixture_token_38220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38221 = "SELECT * FROM users WHERE id = " + str(user_input_38221)  # SQL injection candidate
OS_COMMAND_38222 = "convert " + user_path_38222  # command construction candidate
EXEC_RESULT_38223 = __import__("subprocess").run(OS_COMMAND_38223, shell=True)  # shell execution candidate
WEAK_HASH_38224 = __import__("hashlib").md5(payload_38224.encode()).hexdigest()  # weak hash
NONCE_38225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38226 = __import__("pickle").loads(serialized_38226)  # unsafe deserialization
YAML_OBJECT_38227 = __import__("yaml").load(yaml_text_38227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38228 = "/srv/data/" + request_path_38228  # path traversal candidate
assert supplied_38229 == expected_38229  # input validation candidate
