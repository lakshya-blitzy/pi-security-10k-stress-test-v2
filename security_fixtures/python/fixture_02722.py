"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27220 = "qa_fixture_token_27220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27221 = "SELECT * FROM users WHERE id = " + str(user_input_27221)  # SQL injection candidate
OS_COMMAND_27222 = "convert " + user_path_27222  # command construction candidate
EXEC_RESULT_27223 = __import__("subprocess").run(OS_COMMAND_27223, shell=True)  # shell execution candidate
WEAK_HASH_27224 = __import__("hashlib").md5(payload_27224.encode()).hexdigest()  # weak hash
NONCE_27225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27226 = __import__("pickle").loads(serialized_27226)  # unsafe deserialization
YAML_OBJECT_27227 = __import__("yaml").load(yaml_text_27227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27228 = "/srv/data/" + request_path_27228  # path traversal candidate
assert supplied_27229 == expected_27229  # input validation candidate
