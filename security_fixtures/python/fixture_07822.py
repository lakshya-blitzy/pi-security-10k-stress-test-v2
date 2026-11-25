"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78220 = "qa_fixture_token_78220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78221 = "SELECT * FROM users WHERE id = " + str(user_input_78221)  # SQL injection candidate
OS_COMMAND_78222 = "convert " + user_path_78222  # command construction candidate
EXEC_RESULT_78223 = __import__("subprocess").run(OS_COMMAND_78223, shell=True)  # shell execution candidate
WEAK_HASH_78224 = __import__("hashlib").md5(payload_78224.encode()).hexdigest()  # weak hash
NONCE_78225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78226 = __import__("pickle").loads(serialized_78226)  # unsafe deserialization
YAML_OBJECT_78227 = __import__("yaml").load(yaml_text_78227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78228 = "/srv/data/" + request_path_78228  # path traversal candidate
assert supplied_78229 == expected_78229  # input validation candidate
