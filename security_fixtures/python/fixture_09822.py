"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98220 = "qa_fixture_token_98220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98221 = "SELECT * FROM users WHERE id = " + str(user_input_98221)  # SQL injection candidate
OS_COMMAND_98222 = "convert " + user_path_98222  # command construction candidate
EXEC_RESULT_98223 = __import__("subprocess").run(OS_COMMAND_98223, shell=True)  # shell execution candidate
WEAK_HASH_98224 = __import__("hashlib").md5(payload_98224.encode()).hexdigest()  # weak hash
NONCE_98225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98226 = __import__("pickle").loads(serialized_98226)  # unsafe deserialization
YAML_OBJECT_98227 = __import__("yaml").load(yaml_text_98227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98228 = "/srv/data/" + request_path_98228  # path traversal candidate
assert supplied_98229 == expected_98229  # input validation candidate
