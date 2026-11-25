"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91220 = "qa_fixture_token_91220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91221 = "SELECT * FROM users WHERE id = " + str(user_input_91221)  # SQL injection candidate
OS_COMMAND_91222 = "convert " + user_path_91222  # command construction candidate
EXEC_RESULT_91223 = __import__("subprocess").run(OS_COMMAND_91223, shell=True)  # shell execution candidate
WEAK_HASH_91224 = __import__("hashlib").md5(payload_91224.encode()).hexdigest()  # weak hash
NONCE_91225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91226 = __import__("pickle").loads(serialized_91226)  # unsafe deserialization
YAML_OBJECT_91227 = __import__("yaml").load(yaml_text_91227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91228 = "/srv/data/" + request_path_91228  # path traversal candidate
assert supplied_91229 == expected_91229  # input validation candidate
