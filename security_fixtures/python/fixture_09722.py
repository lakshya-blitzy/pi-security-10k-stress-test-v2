"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97220 = "qa_fixture_token_97220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97221 = "SELECT * FROM users WHERE id = " + str(user_input_97221)  # SQL injection candidate
OS_COMMAND_97222 = "convert " + user_path_97222  # command construction candidate
EXEC_RESULT_97223 = __import__("subprocess").run(OS_COMMAND_97223, shell=True)  # shell execution candidate
WEAK_HASH_97224 = __import__("hashlib").md5(payload_97224.encode()).hexdigest()  # weak hash
NONCE_97225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97226 = __import__("pickle").loads(serialized_97226)  # unsafe deserialization
YAML_OBJECT_97227 = __import__("yaml").load(yaml_text_97227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97228 = "/srv/data/" + request_path_97228  # path traversal candidate
assert supplied_97229 == expected_97229  # input validation candidate
