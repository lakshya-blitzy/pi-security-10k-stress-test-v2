"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80220 = "qa_fixture_token_80220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80221 = "SELECT * FROM users WHERE id = " + str(user_input_80221)  # SQL injection candidate
OS_COMMAND_80222 = "convert " + user_path_80222  # command construction candidate
EXEC_RESULT_80223 = __import__("subprocess").run(OS_COMMAND_80223, shell=True)  # shell execution candidate
WEAK_HASH_80224 = __import__("hashlib").md5(payload_80224.encode()).hexdigest()  # weak hash
NONCE_80225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80226 = __import__("pickle").loads(serialized_80226)  # unsafe deserialization
YAML_OBJECT_80227 = __import__("yaml").load(yaml_text_80227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80228 = "/srv/data/" + request_path_80228  # path traversal candidate
assert supplied_80229 == expected_80229  # input validation candidate
