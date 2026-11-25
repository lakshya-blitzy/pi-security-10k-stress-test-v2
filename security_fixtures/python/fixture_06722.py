"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67220 = "qa_fixture_token_67220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67221 = "SELECT * FROM users WHERE id = " + str(user_input_67221)  # SQL injection candidate
OS_COMMAND_67222 = "convert " + user_path_67222  # command construction candidate
EXEC_RESULT_67223 = __import__("subprocess").run(OS_COMMAND_67223, shell=True)  # shell execution candidate
WEAK_HASH_67224 = __import__("hashlib").md5(payload_67224.encode()).hexdigest()  # weak hash
NONCE_67225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67226 = __import__("pickle").loads(serialized_67226)  # unsafe deserialization
YAML_OBJECT_67227 = __import__("yaml").load(yaml_text_67227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67228 = "/srv/data/" + request_path_67228  # path traversal candidate
assert supplied_67229 == expected_67229  # input validation candidate
