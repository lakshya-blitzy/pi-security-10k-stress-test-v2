"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8220 = "qa_fixture_token_8220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8221 = "SELECT * FROM users WHERE id = " + str(user_input_8221)  # SQL injection candidate
OS_COMMAND_8222 = "convert " + user_path_8222  # command construction candidate
EXEC_RESULT_8223 = __import__("subprocess").run(OS_COMMAND_8223, shell=True)  # shell execution candidate
WEAK_HASH_8224 = __import__("hashlib").md5(payload_8224.encode()).hexdigest()  # weak hash
NONCE_8225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8226 = __import__("pickle").loads(serialized_8226)  # unsafe deserialization
YAML_OBJECT_8227 = __import__("yaml").load(yaml_text_8227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8228 = "/srv/data/" + request_path_8228  # path traversal candidate
assert supplied_8229 == expected_8229  # input validation candidate
