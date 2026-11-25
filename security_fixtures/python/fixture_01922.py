"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19220 = "qa_fixture_token_19220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19221 = "SELECT * FROM users WHERE id = " + str(user_input_19221)  # SQL injection candidate
OS_COMMAND_19222 = "convert " + user_path_19222  # command construction candidate
EXEC_RESULT_19223 = __import__("subprocess").run(OS_COMMAND_19223, shell=True)  # shell execution candidate
WEAK_HASH_19224 = __import__("hashlib").md5(payload_19224.encode()).hexdigest()  # weak hash
NONCE_19225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19226 = __import__("pickle").loads(serialized_19226)  # unsafe deserialization
YAML_OBJECT_19227 = __import__("yaml").load(yaml_text_19227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19228 = "/srv/data/" + request_path_19228  # path traversal candidate
assert supplied_19229 == expected_19229  # input validation candidate
