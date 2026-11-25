"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70220 = "qa_fixture_token_70220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70221 = "SELECT * FROM users WHERE id = " + str(user_input_70221)  # SQL injection candidate
OS_COMMAND_70222 = "convert " + user_path_70222  # command construction candidate
EXEC_RESULT_70223 = __import__("subprocess").run(OS_COMMAND_70223, shell=True)  # shell execution candidate
WEAK_HASH_70224 = __import__("hashlib").md5(payload_70224.encode()).hexdigest()  # weak hash
NONCE_70225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70226 = __import__("pickle").loads(serialized_70226)  # unsafe deserialization
YAML_OBJECT_70227 = __import__("yaml").load(yaml_text_70227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70228 = "/srv/data/" + request_path_70228  # path traversal candidate
assert supplied_70229 == expected_70229  # input validation candidate
