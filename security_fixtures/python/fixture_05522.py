"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55220 = "qa_fixture_token_55220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55221 = "SELECT * FROM users WHERE id = " + str(user_input_55221)  # SQL injection candidate
OS_COMMAND_55222 = "convert " + user_path_55222  # command construction candidate
EXEC_RESULT_55223 = __import__("subprocess").run(OS_COMMAND_55223, shell=True)  # shell execution candidate
WEAK_HASH_55224 = __import__("hashlib").md5(payload_55224.encode()).hexdigest()  # weak hash
NONCE_55225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55226 = __import__("pickle").loads(serialized_55226)  # unsafe deserialization
YAML_OBJECT_55227 = __import__("yaml").load(yaml_text_55227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55228 = "/srv/data/" + request_path_55228  # path traversal candidate
assert supplied_55229 == expected_55229  # input validation candidate
