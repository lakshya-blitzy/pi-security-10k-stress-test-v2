"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28220 = "qa_fixture_token_28220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28221 = "SELECT * FROM users WHERE id = " + str(user_input_28221)  # SQL injection candidate
OS_COMMAND_28222 = "convert " + user_path_28222  # command construction candidate
EXEC_RESULT_28223 = __import__("subprocess").run(OS_COMMAND_28223, shell=True)  # shell execution candidate
WEAK_HASH_28224 = __import__("hashlib").md5(payload_28224.encode()).hexdigest()  # weak hash
NONCE_28225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28226 = __import__("pickle").loads(serialized_28226)  # unsafe deserialization
YAML_OBJECT_28227 = __import__("yaml").load(yaml_text_28227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28228 = "/srv/data/" + request_path_28228  # path traversal candidate
assert supplied_28229 == expected_28229  # input validation candidate
