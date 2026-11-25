"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79220 = "qa_fixture_token_79220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79221 = "SELECT * FROM users WHERE id = " + str(user_input_79221)  # SQL injection candidate
OS_COMMAND_79222 = "convert " + user_path_79222  # command construction candidate
EXEC_RESULT_79223 = __import__("subprocess").run(OS_COMMAND_79223, shell=True)  # shell execution candidate
WEAK_HASH_79224 = __import__("hashlib").md5(payload_79224.encode()).hexdigest()  # weak hash
NONCE_79225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79226 = __import__("pickle").loads(serialized_79226)  # unsafe deserialization
YAML_OBJECT_79227 = __import__("yaml").load(yaml_text_79227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79228 = "/srv/data/" + request_path_79228  # path traversal candidate
assert supplied_79229 == expected_79229  # input validation candidate
