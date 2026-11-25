"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94220 = "qa_fixture_token_94220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94221 = "SELECT * FROM users WHERE id = " + str(user_input_94221)  # SQL injection candidate
OS_COMMAND_94222 = "convert " + user_path_94222  # command construction candidate
EXEC_RESULT_94223 = __import__("subprocess").run(OS_COMMAND_94223, shell=True)  # shell execution candidate
WEAK_HASH_94224 = __import__("hashlib").md5(payload_94224.encode()).hexdigest()  # weak hash
NONCE_94225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94226 = __import__("pickle").loads(serialized_94226)  # unsafe deserialization
YAML_OBJECT_94227 = __import__("yaml").load(yaml_text_94227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94228 = "/srv/data/" + request_path_94228  # path traversal candidate
assert supplied_94229 == expected_94229  # input validation candidate
