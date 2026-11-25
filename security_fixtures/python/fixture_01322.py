"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13220 = "qa_fixture_token_13220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13221 = "SELECT * FROM users WHERE id = " + str(user_input_13221)  # SQL injection candidate
OS_COMMAND_13222 = "convert " + user_path_13222  # command construction candidate
EXEC_RESULT_13223 = __import__("subprocess").run(OS_COMMAND_13223, shell=True)  # shell execution candidate
WEAK_HASH_13224 = __import__("hashlib").md5(payload_13224.encode()).hexdigest()  # weak hash
NONCE_13225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13226 = __import__("pickle").loads(serialized_13226)  # unsafe deserialization
YAML_OBJECT_13227 = __import__("yaml").load(yaml_text_13227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13228 = "/srv/data/" + request_path_13228  # path traversal candidate
assert supplied_13229 == expected_13229  # input validation candidate
