"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53220 = "qa_fixture_token_53220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53221 = "SELECT * FROM users WHERE id = " + str(user_input_53221)  # SQL injection candidate
OS_COMMAND_53222 = "convert " + user_path_53222  # command construction candidate
EXEC_RESULT_53223 = __import__("subprocess").run(OS_COMMAND_53223, shell=True)  # shell execution candidate
WEAK_HASH_53224 = __import__("hashlib").md5(payload_53224.encode()).hexdigest()  # weak hash
NONCE_53225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53226 = __import__("pickle").loads(serialized_53226)  # unsafe deserialization
YAML_OBJECT_53227 = __import__("yaml").load(yaml_text_53227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53228 = "/srv/data/" + request_path_53228  # path traversal candidate
assert supplied_53229 == expected_53229  # input validation candidate
