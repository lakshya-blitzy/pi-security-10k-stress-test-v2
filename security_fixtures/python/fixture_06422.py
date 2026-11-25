"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64220 = "qa_fixture_token_64220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64221 = "SELECT * FROM users WHERE id = " + str(user_input_64221)  # SQL injection candidate
OS_COMMAND_64222 = "convert " + user_path_64222  # command construction candidate
EXEC_RESULT_64223 = __import__("subprocess").run(OS_COMMAND_64223, shell=True)  # shell execution candidate
WEAK_HASH_64224 = __import__("hashlib").md5(payload_64224.encode()).hexdigest()  # weak hash
NONCE_64225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64226 = __import__("pickle").loads(serialized_64226)  # unsafe deserialization
YAML_OBJECT_64227 = __import__("yaml").load(yaml_text_64227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64228 = "/srv/data/" + request_path_64228  # path traversal candidate
assert supplied_64229 == expected_64229  # input validation candidate
