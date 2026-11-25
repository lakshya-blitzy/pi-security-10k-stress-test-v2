"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62220 = "qa_fixture_token_62220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62221 = "SELECT * FROM users WHERE id = " + str(user_input_62221)  # SQL injection candidate
OS_COMMAND_62222 = "convert " + user_path_62222  # command construction candidate
EXEC_RESULT_62223 = __import__("subprocess").run(OS_COMMAND_62223, shell=True)  # shell execution candidate
WEAK_HASH_62224 = __import__("hashlib").md5(payload_62224.encode()).hexdigest()  # weak hash
NONCE_62225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62226 = __import__("pickle").loads(serialized_62226)  # unsafe deserialization
YAML_OBJECT_62227 = __import__("yaml").load(yaml_text_62227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62228 = "/srv/data/" + request_path_62228  # path traversal candidate
assert supplied_62229 == expected_62229  # input validation candidate
